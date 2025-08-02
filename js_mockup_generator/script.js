window.onload = function () {
  const canvas = document.getElementById("mockupCanvas");
  const ctx = canvas.getContext("2d");

  const productImage = new Image();
  productImage.src = "../assets/generated_image.png";

  productImage.onload = () => {
    // Draw the product image to fill the canvas
    ctx.drawImage(productImage, 0, 0, canvas.width, canvas.height);
  };

  productImage.onerror = () => {
    console.error("❌ Failed to load product image. Check the path and file name.");
  };
};
