const overlay = document.getElementById("full-img-overlay");
overlay.style.visibility = 'hidden'

document.getElementById("close-full-img-icon").addEventListener("click", function(event){
    event.preventDefault();
    overlay.style.visibility = 'hidden';  
  });

  // document.getElementById("img-small-view").addEventListener("click", function(event){
  //   event.preventDefault();
  //    overlay.style.visibility = 'visible';
  // });

  document.getElementById("full-img-text-btn").addEventListener("click", function(event){
    event.preventDefault();
     overlay.style.visibility = 'visible';
  });