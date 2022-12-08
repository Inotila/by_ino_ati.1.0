// full image view

const overlay = document.getElementById("full-img-overlay");
overlay.style.visibility = 'hidden';

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
  shareOverlay.style.visibility = 'hidden';

  document.getElementById("share-btn").addEventListener("click", function(event){
    event.preventDefault();
    shareOverlay.style.visibility = 'visible';
  });

  document.getElementById("close-share-div-icon").addEventListener("click", function(event){
    event.preventDefault();
    shareOverlay.style.visibility = 'hidden';  
  });
  
  window.onload = () => {
    
  }


  // zoom in functionality

  const container = document.getElementById('img-container')
  const normalImage = document.getElementById('normal-image')
  const lens = document.getElementById('lens')
  const result = document.getElementById('result')

  const containerRect = container.getBoundingClientRect()
  const imageRect = normalImage.getBoundingClientRect()
  const lensRect = lens.getBoundingClientRect()
  const resultRect = result.getBoundingClientRect()

  container.addEventListener('mousemove', zoomImage)

  function zoomImage(e){
    console.log('zoom image', e.clientX, e.clientY)

    let x = e.clientX - containerRect.left - lensRect.width / 2;
    let y = e.clientY - containerRect.top - lensRect.height / 2;

    let minX = 0;
    let minY = 0;
    let maxX = containerRect.width - lensRect.width;

    lens.style.left = x + "px";
    lens.style.top = y + "px";
  }