var myLine;
var loadChartData;
var totalChartData;
var latencyChartData;
var labelChartData;
function getTimelineStart(start){
	document.getElementById("pickerStartDay").value=start.day
	document.getElementById("pickerStartMonth").value=start.month
	document.getElementById("pickerStartYear").value=start.year;
	document.getElementById("pickerStartHours").value="00";
	document.getElementById("pickerStartMinutes").value="00";
}

function getTimelineEnd(end){
	document.getElementById("pickerEndDay").value=end.day
	document.getElementById("pickerEndMonth").value=end.month
	document.getElementById("pickerEndYear").value=end.year;
	document.getElementById("pickerEndHours").value="23";
	document.getElementById("pickerEndMinutes").value="59";
}

function setSource(){

	var source = document.getElementById("sources").value;
	var src = "../measurements/"+source+".js";
	
	var head = document.getElementsByTagName('head')[0];
	//use class, as we can't reference by id
	var elements = head.getElementsByClassName("timings_js");
	for (var i=0; i<elements.length; i++){
		elements[i].parentNode.removeChild(elements[i]);
	}
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = src;
	script.className = "timings_js";
	script.async = false;
	script.onload = function () {
        //console.log('Loaded script:' + src);
		setupData();
    };
	head.appendChild(script);
}

function setupData(){
	var start = timings_js_data[0].timestamp;
	var end = timings_js_data.slice(-1)[0].timestamp;
	var startDate = new Date(start*1);
	var endDate = new Date(end*1);
	var sD = startDate.getDate()+"."+(startDate.getMonth()+1)+"."+startDate.getFullYear()+" "+setDisplayTime(startDate.getHours(), startDate.getMinutes());
	var eD = endDate.getDate()+"."+(endDate.getMonth()+1)+"."+endDate.getFullYear()+" "+setDisplayTime(endDate.getHours(), endDate.getMinutes());
	document.getElementById("availability").innerHTML = sD+" - "+eD;
	if (timings_js_data.length > 100){
		graphData = timings_js_data.slice(-100);
	}
	else{
		graphData = timings_js_data;
	}
	start = graphData[0].timestamp;
	end = graphData.slice(-1)[0].timestamp;
	startDate = new Date(start*1);
	endDate = new Date(end*1);
	document.getElementById("pickerStartDay").value = startDate.getDate();
	document.getElementById("pickerStartMonth").value = startDate.getMonth()+1;
	document.getElementById("pickerStartYear").value = startDate.getFullYear();
	document.getElementById("pickerStartHours").value = startDate.getHours();
	document.getElementById("pickerStartMinutes").value = startDate.getMinutes();
	
	document.getElementById("pickerEndDay").value = endDate.getDate();
	document.getElementById("pickerEndMonth").value = endDate.getMonth()+1;
	document.getElementById("pickerEndYear").value = endDate.getFullYear();
	document.getElementById("pickerEndHours").value = endDate.getHours();
	document.getElementById("pickerEndMinutes").value = endDate.getMinutes()+1;
	setGraphData(graphData);
}


function setGraphData(graphData){
	
	var graphData = (typeof graphData === 'undefined') ? timings_js_data : graphData;
	
	var source = document.getElementById("sources").value;
	
	var sd = document.getElementById("pickerStartDay").value;
	var sm = document.getElementById("pickerStartMonth").value;
	var sy = document.getElementById("pickerStartYear").value;
	var sh = document.getElementById("pickerStartHours").value;
	var smi = document.getElementById("pickerStartMinutes").value;
	
	var ed = document.getElementById("pickerEndDay").value;
	var em = document.getElementById("pickerEndMonth").value;
	var ey = document.getElementById("pickerEndYear").value;
	var eh = document.getElementById("pickerEndHours").value;
	var emi = document.getElementById("pickerEndMinutes").value;
	var sDate = new Date(sy, sm-1, sd, sh, smi, 0);
	var eDate = new Date(ey, em-1, ed, eh, emi, 0);
	var start=sDate.getTime();
	var end=eDate.getTime();
	
	//var ts=new Array();
	//var lt=new Array();
	loadChartData = new Array();
	totalChartData = new Array();
	latencyChartData = new Array();
	labelChartData = new Array();
	if(start < 0){
		alert("Check if you chose source file and Start date");
		return;
	}
	if(end < 0){
		alert("You must put End date");
		return;
	}
	if(start > end){
		alert("Wrong dates selected! End date is earlier than Start date.");
		return;
	}
	var isMilliseconds = document.getElementById("milliseconds").checked;
	var from = document.getElementById("dataFrom").value;
	var datafrom = isNaN(filterFloat(from)) ? 0 : filterFloat(from);
	var to = document.getElementById("dataTo").value;
	var datato = isNaN(filterFloat(to)) ? 0 : filterFloat(to);
	var critical = document.getElementById("critical").value;
	var criticalValue = isNaN(filterFloat(critical)) ? 0 : filterFloat(critical);
	var crit = 0;
	var ncrit = 0;
	var criticalElement = document.getElementById("critical").value;
	if(isMilliseconds == false){
		datafrom = datafrom*1000;
		datato=datato*1000;
		criticalValue=criticalValue*1000;
	}
	var counter=0;
	for (i=0;i<graphData.length;i++){
		var timestamp = graphData[i].timestamp;
		if(timestamp >= start && timestamp <= end){
			//var ltValue = parseInt(graphData[i].load);
			if(datato != 0 && datafrom != 0){ // from 99 to 99
				if(ltValue >= datafrom && ltValue <= datato){
					collectGraphData(graphData[i], isMilliseconds);
				}	
			}else if(datato != 0 && datafrom == 0){ // from _ to 99
				if(ltValue <= datato){
					val = dataFilter(ltUnit, ltValue, timestamp);
					ts.push(val[0]);
					lt.push(val[1]);
					counter = counter + 1;
					cr = criticalValueSet(ltValue,criticalValue,crit,ncrit);
					crit = cr[0];
					ncrit = cr[1];
				}
			}else if(datato == 0 && datafrom != 0){ // from 99 to _
				if(ltValue >= datafrom){
					val = dataFilter(ltUnit, ltValue, timestamp);
					ts.push(val[0]);
					lt.push(val[1]);
					counter = counter + 1;
					cr = criticalValueSet(ltValue,criticalValue,crit,ncrit);
					crit = cr[0];
					ncrit = cr[1];
				}
			}else{  // from _ to _
				collectGraphData(graphData[i], isMilliseconds);
			}
		}
	}
	document.getElementById("reportName").innerHTML = "<b>"+source+"</b>";
	document.getElementById("reportStartDate").innerHTML = sDate.getDate()+"."+(sDate.getMonth()+1)+"."+sDate.getFullYear();
	document.getElementById("reporEndDate").innerHTML = eDate.getDate()+"."+(eDate.getMonth()+1)+"."+eDate.getFullYear();						
	document.getElementById("reportStartTime").innerHTML = setDisplayTime(sDate.getHours(), sDate.getMinutes());
	document.getElementById("reportEndTime").innerHTML = setDisplayTime(eDate.getHours(), eDate.getMinutes());
	
	drawChats(criticalValue);
}

function collectGraphData(data, isMilliseconds){
	//load time
	if (data.load){
		var loadTime = isMilliseconds == true ? parseInt(data.load) : parseInt(data.load) / 1000;
		loadChartData.push(loadTime);
	}
	if (data.total){
		var totalTime = isMilliseconds == true ? parseInt(data.total) : parseInt(data.total) / 1000;
		totalChartData.push(totalTime);
	}
	if (data.latency){
		var latencyTime = isMilliseconds == true ? parseInt(data.latency) : parseInt(data.latency) / 1000;
		latencyChartData.push(latencyTime);
	}
	labelChartData.push(formatTimestamp(data.timestamp));
}

function drawChats(criticalValue){
	if(labelChartData==""){
		alert("No data for this filter");
		return;
	}
	
	var measurement = document.getElementById("measurement").value;
	var totalData = {
			label: "total time",
			fillColor : "rgba(151,187,205,0.2)",
			strokeColor : "rgba(151,187,205,1)",
			pointColor : "rgba(151,187,205,1)",
			pointStrokeColor : "#fff",
			pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
			data : totalChartData
		};
	var loadData = {
			label: "load time",
			fillColor : "rgba(200,200,200,0.2)",
			strokeColor : "rgba(200,200,200,1)",
			pointColor : "rgba(200,200,200,1)",
			pointStrokeColor : "#fff",
			pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(200,200,200,1)",
			data : loadChartData
		};
	var latencyData = {
			label: "latency",
			fillColor : "rgba(110,110,110,0.05)",
			strokeColor : "rgba(110,110,110,1)",
			pointColor : "rgba(110,110,110,1)",
			pointStrokeColor : "#fff",
			pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(110,110,110,1)",
			data : latencyChartData
		};
	var lineDataset = new Array;
	if (measurement == 'all'){
		lineDataset.push(totalData);
		lineDataset.push(loadData);
		lineDataset.push(latencyData);
	}
	else if(measurement == 'load time'){
		if (loadChartData.length == 0){
			alert("No data for 'load' timings");
			return;
		}
		loadData.fillColor = "rgba(200,200,200,0.5)";
		lineDataset.push(loadData);
	}
	else if(measurement == 'total time'){
		if (totalChartData.length == 0){
			alert("No data for 'total' timings");
			return;
		}
		totalData.fillColor = "rgba(151,187,205,0.5)";
		lineDataset.push(totalData);
	}
	else if(measurement == 'latency'){
		console.log(latencyChartData.length)
		if (latencyChartData.length == 0){
			alert("No data for 'latency' timings");
			return;
		}
		latencyData.fillColor = "rgba(110,110,110,0.5)";
		lineDataset.push(latencyData);
	}
	var lineChartData = {
	labels : labelChartData,
	datasets : lineDataset
	};
	if (myLine){
		myLine.destroy()
	}
	myLine = new Chart(document.getElementById("canvas").getContext("2d")).Line(lineChartData, {
																				multiTooltipTemplate: "<%= value %> - <%= datasetLabel %>"
																				});
	
	// ================ donut graph ================	
	if(!criticalValue){
		document.getElementById("results").innerHTML = "Results: <b>"+labelChartData.length + "</b>";
	}else{
		document.getElementById("results").innerHTML = "Results: <b>"+labelChartData.length + "</b><br>Critical: <b>"+crit+"</b><br>Not critical: <b>"+ncrit+"</b>";
		var ctx = document.getElementById("donut").getContext("2d");
		var data = [{value: ncrit,color:"#A4C9AC"},{value : crit,color : "#424043"}];
		var options = {segmentShowStroke : false, animationSteps : 50, percentageInnerCutout : 70};
		var donutChart = new Chart(ctx).Doughnut(data, options);
	}
	// ================ donut graph ================
}

var filterFloat = function (value) {
    if(/^(\-|\+)?([0-9]+(\.[0-9]+)?|Infinity)$/
      .test(value))
      return Number(value);
  return NaN;
}

function setDisplayTime(hours, minutes){
	var hh=hours;
	var mm=minutes;
	var val;
	if(hours<10){hh="0"+hours.toString();}
	if(minutes<10){mm="0"+minutes.toString();}
	val = hh+":"+mm;
	return val;
}

function criticalValueSet(lt, criticalValue, critical, notCritical){
	if(lt < criticalValue){notCritical = notCritical + 1;} 
	else {critical = critical + 1;}
	//console.log("critical value: " + criticalValue + ", lt: "+lt+", critical:"+critical+", not critical:"+notCritical);
	return [critical,notCritical];
}

function formatTimestamp(timestamp){
	var d = new Date(timestamp*1);
	var ts = d.getDate()+"."+(d.getMonth()+1)+"."+d.getFullYear()+" "+setDisplayTime(d.getHours(),d.getMinutes());
	return ts;
}
