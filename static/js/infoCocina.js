const images = document.querySelectorAll('.img');
const containerImage = document.querySelector('.container_img');
const imageContainer = document.querySelector('.img-show');
const copy = document.querySelector('.copy');
const closeModal = document.querySelector('.close');

images.forEach( image => {
    image.addEventListener('click', ()=> {
        addImage(image.getAttribute('src'), image.getAttribute('alt'));
    })
})

const addImage = (srcImage, altImage)=>{
    containerImage.classList.toggle('move');
    imageContainer.classList.toggle('showImage');
    imageContainer.src = srcImage;
    copy.innerHTML = altImage
}

closeModal.addEventListener('click', ()=>{
    containerImage.classList.toggle('move');
    imageContainer.classList.toggle('showImage');
})