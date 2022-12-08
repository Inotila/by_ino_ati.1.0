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

  result.style.backgroundImage = `url(${normalImage.src})`

  function zoomImage(e){
    const { x, y} = getMousePosition(e);

    lens.style.left = x + "px";
    lens.style.top = y + "px";

    let fx = resultRect.width / lensRect.width 
    let fy = resultRect.height / lensRect.height     

    result.style.backgroundSize = `${imageRect.width * fx}px ${imageRect.height * fy}px`;
    result.style.backgroundPosition = `-${x * fx}px -${y * fy}px`
  }

  function getMousePosition(e){
    let x = e.clientX - containerRect.left - lensRect.width / 2;
    let y = e.clientY - containerRect.top - lensRect.height / 2;

    // limits the lens/mouse in the box of the image
    let minX = 0;
    let minY = 0;
    let maxX = containerRect.width - lensRect.width;
    let maxY = containerRect.height - lensRect.height;

    if(x <= minX){
      x = minX;
    } else if ( x >= maxX){
      x = maxX;
    }

    if(y <= minY){
      y = minY;
    } else if ( y >= maxY){
      y = maxY;
    }

    return{ x, y}
  }