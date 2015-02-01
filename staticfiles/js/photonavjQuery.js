/*
 * 	PhotoNavigation the jQuery version
 * 	A Javascript Module by Gaya Kessler
 * 	Version 1.0
 * 	Date: 09-04-09
 * 
 */
 
var PhotoNav = {
	
	statusArr: new Array(),
	debugging: false,
	containerWidth: 0,
	container: "",
	photo: "",
	photoWidth: 0,
	
		
	init: function(id, width, width2, debugging) {
		//catch undefined vars	
		if (typeof(debugging) != 'undefined') {
			PhotoNav.debugging = debugging;
		} else {
			PhotoNav.debugging = false;
		}
		
		//make room in status array
		PhotoNav.statusArr[0] = "";
		PhotoNav.statusArr[1] = "";
		
		$('#' + id).mousemove(function(event){
			var x = event.pageX - this.offsetLeft;
			var y = event.pageY - this.offsetTop;
			
			var perc = (100 / (PhotoNav.containerWidth / x));
			
			PhotoNav.posPicture(perc);
			
			PhotoNav.addStatus('X: '+x+'  Y:'+y + ' '+perc+'%');
	    });
		
		//set some object vars
		PhotoNav.container = id;
		PhotoNav.containerWidth = width;
		PhotoNav.photoWidth = width2;

		$("#" + id + " .fixed").each(function(i) {
			PhotoNav.photo = $(this);
			PhotoNav.photo.css({"width":width2 + "px"});
		});
	},
	
	addStatus: function(str) {
		if (PhotoNav.debugging == true) {
			PhotoNav.statusArr.unshift(str);
			PhotoNav.statusArr.splice(3, 10);
			
			$("#status").html("");
			
			for (var i = 2; i > 0; i = i - 1) {
				$("#status").html(PhotoNav.statusArr[i] + "<br />" + $("#status").html());
			}
		}
	},
	
	posPicture: function(x) {
		var full = PhotoNav.photoWidth;
		full = full - PhotoNav.containerWidth;
		var curX = full * (x / 100);
		
		if (curX < 0) {
			curX = 0;
		}
		
		PhotoNav.addStatus("Mouse X container: " + curX);
		
		PhotoNav.photo.css({
			marginLeft: "-"+curX+"px"
		});
	}
}