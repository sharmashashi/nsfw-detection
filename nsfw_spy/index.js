const { NsfwSpy } = require('@nsfwspy/node');

const filePath = "../image.jpg";
const nsfwSpy = new NsfwSpy("file://models/mobilenet-v1.0.0/model.json");

async function classifyImage() {
  try {
    await nsfwSpy.load(); // Load the model
    const result = await nsfwSpy.classifyImageFile(filePath); // Classify the image
    console.log(result);
  } catch (error) {
    console.error("Error:", error);
  }
}

classifyImage();
