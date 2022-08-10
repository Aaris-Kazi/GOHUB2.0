
function autocomplete(inp, arr) {
	  var currentFocus;
	  /*execute a function when someone writes in the text field:*/
	  inp.addEventListener("change", function(e) {
		  var a, b, i, val = this.value;
		  /*close any already open lists of autocompleted values*/
		  closeAllLists();
		  if (!val) { return false;}
		  currentFocus = -1;
		  /*create a DIV element that will contain the items (values):*/
		  a = document.createElement("DIV");
		  a.setAttribute("id", this.id + "autocomplete-list");
		  a.setAttribute("class", "autocomplete-items");
		  /*append the DIV element as a child of the autocomplete container:*/
		  this.parentNode.appendChild(a);
		  /*for each item in the array...*/
		  for (i = 0; i < arr.length; i++) {
			/*check if the item starts with the same letters as the text field value:*/
			if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
			  /*create a DIV element for each matching element:*/
			  b = document.createElement("div");
              b.setAttribute('class', 'suggestions')
			  /*make the matching letters bold:*/
			  b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
			  b.innerHTML += arr[i].substr(val.length);
			  /*insert a input field that will hold the current array item's value:*/
			  b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
			  /*execute a function when someone clicks on the item value (DIV element):*/
			  b.addEventListener("click", function(e) {
				  /*insert the value for the autocomplete text field:*/
				  inp.value = this.getElementsByTagName("input")[0].value;
				  /*close the list of autocompleted values,
				  (or any other open lists of autocompleted values:*/
				  closeAllLists();
			  });
			  a.appendChild(b);
			}
		  }
	  });
	  /*execute a function presses a key on the keyboard:*/
	  inp.addEventListener("keydown", function(e) {
		  var x = document.getElementById(this.id + "autocomplete-list");
          x = x.getElementsByTagName("div")
		  if (x) x = x.setAttribute('class', 'suggestions');
		  if (e.keyCode == 40) {
			currentFocus++;
			/*and and make the current item more visible:*/
			addActive(x);
		  } else if (e.keyCode == 38) { //up
			/*If the arrow UP key is pressed,
			decrease the currentFocus variable:*/
			currentFocus--;
			/*and and make the current item more visible:*/
			addActive(x);
		  } else if (e.keyCode == 13) {
			/*If the ENTER key is pressed, prevent the form from being submitted,*/
			e.preventDefault();
			if (currentFocus > -1) {
			  /*and simulate a click on the "active" item:*/
			  if (x) x[currentFocus].click();
			}
		  }
	  });
	  function addActive(x) {
		/*a function to classify an item as "active":*/
		if (!x) return false;
		/*start by removing the "active" class on all items:*/
		removeActive(x);
		if (currentFocus >= x.length) currentFocus = 0;
		if (currentFocus < 0) currentFocus = (x.length - 1);
		/*add class "autocomplete-active":*/
		x[currentFocus].classList.add("autocomplete-active");
	  }
	  function removeActive(x) {
		/*a function to remove the "active" class from all autocomplete items:*/
		for (var i = 0; i < x.length; i++) {
		  x[i].classList.remove("autocomplete-active");
		}
	  }
	  function closeAllLists(elmnt) {
		/*close all autocomplete lists in the document,
		except the one passed as an argument:*/
		var x = document.getElementsByClassName("autocomplete-items");
		for (var i = 0; i < x.length; i++) {
		  if (elmnt != x[i] && elmnt != inp) {
			x[i].parentNode.removeChild(x[i]);
		  }
		}
	  }
	  /*execute a function when someone clicks in the document:*/
	  document.addEventListener("click", function (e) {
		  closeAllLists(e.target);
	  });
	}
	
	/*An array containing all the country names in the world:*/
	var place= ["Hampi","Haridwar","Kerala Backwaters","Lakshadeep Island","Pushkar Fair","Varanasi Ghats","Cheraman Juma Masjid","Jama Mosque","Mecca Masjid","Old Juma Masjid","Ziarat Shareef","Adina Masjid","Charminar","Ajanta Ellora","Charminar","Fatehpur Sikri","Gateway of India","Humayun\'s Tomb","India Gate","Qutub Minar","Taj Mahal","Basilica of Bom Jesus","Chapel of St. Catherine","Gundala Church","Holy Trinity Church","Our Lady of the Rosary\'s Church","Reis Magos Church","St. Joseph\'s Cathedral","St. Francis of Assissi\'s Church","St. Mary\'s Church","he Cross of Miracles\'s Church","The Sacred Heart\'s Church","Adventure Islands","Entertainment City","Essel World","Fun n Food Village","Gujarat Science City","Kingdom of Dreams","Nicco Park","Ocean Park","Veega Land","Wonder La","Baba Amarnath Temple","Golden Temple","Lord Jagannath Temple","Kashi Vishwanath Temple","Khajuraho Temples","Konark Sun Temple","Ranakpur Jain Temples","Shri Meenakshi - Sundareshwarar Temple","Siddhivinayak Temple","Somnath Temple","Thanjavur Temple","Venkataswara Tirupati Balaji Templ","Brindavan Garden","Chambal Garden","Chashme Shahi Garden","Indian Botanical Garden","Lal Bagh Gardens","Lodhi Garden Mughal Gardens","Pinjore Garden","Rock Garden","Shalimar Bag","Alisagar Deer Park","Bandhavgarh National Park","Bori Wildlife Sanctuary","Hazaribagh Sanctuary","Gir National Park and Sanctuary","Hazaribagh Sanctuary","Kaziranga National Park","Manas Wildlife Sanctuary","Lonavala","Keoladeo National Park","Nanda Devi National Park","Sundarbans National Par","Barehipani Waterfalls","Dudhsagar Waterfalls","Jog Waterfalls","Jonha Waterfalls","Kunchikal Waterfalls","Kune Waterfalls","Langshiang Waterfalls","Meenmutty Waterfalls","Nohkalikai Waterfalls","Shivanasamudra Waterfalls","Chandratal Lake","Dal Lake","Hussain Sagar Lake","Loktak Lake","Osman Sagar Lake","Pushkar Lake","Roopkund Lake","Vembanad Lake","Wular Lake","Bhimtal Lake","Chilka Lake","Dal Lake","Darjeeling","Dehradun","Gangtok","Gangtok","Gangtok","Kodaikanal","Kullu and Manali","Mount Abu","Mussoorie","Ooty","Shillong","Shimla","Srinagar","Agra Fort","Amber Fort","Chittorgarh Fort","Fort William","Golconda Fort","Jaisalmer Fort","Kangra Fort","Red Fort or Lal Qila","Qila Mubarak","Ranthambhore Fort","Bir Singh Palace","Chail Palace","Jaipur City Palace","Jaivilas Palace","Jal Mahal","Lake Palace","Lalgarh Palace","Salim Singh ki Haveli","Udaipur City Palace","Umaid Bhawan Palace"];
	
	
	/*initiate the autocomplete function on the "cities" element, and pass along the place array as possible autocomplete values:*/
autocomplete(document.getElementById("location"), place);
	
