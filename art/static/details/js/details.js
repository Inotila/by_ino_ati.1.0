// full image view

const overlay = document.getElementById("full-img-overlay");
overlay.style.visibility = 'hidden'

document.getElementById("close-full-img-icon").addEventListener("click", function(event){
    event.preventDefault();
    overlay.style.visibility = 'hidden';  
  });

  document.getElementById("details-img-full-view-anchor").addEventListener("click", function(event){
    event.preventDefault();
     overlay.style.visibility = 'visible';
  });

  document.getElementById("full-img-text-btn").addEventListener("click", function(event){
    event.preventDefault();
     overlay.style.visibility = 'visible';
  });

  // share button

  const shareOverlay = document.getElementById("share-div-overlay");
  shareOverlay.style.visibility = 'hidden'

  document.getElementById("share-btn").addEventListener("click", function(event){
    event.preventDefault();
    shareOverlay.style.visibility = 'visible';
  });

  document.getElementById("close-share-div-icon").addEventListener("click", function(event){
    event.preventDefault();
    shareOverlay.style.visibility = 'hidden';  
  });
  
