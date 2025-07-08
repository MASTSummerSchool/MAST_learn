//% color="#F7AD45" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Capture image from webcam [CAMERA_INDEX]" blockType="reporter"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    export function capture_webcam_image(parameter: any, block: any) {
        let camera_index = parameter.CAMERA_INDEX.code;
        Generator.addImport(`from learn import capture_webcam_image`);
        Generator.addCode(`capture_webcam_image(${camera_index})`);

        // Add comments
        Generator.addCode(`# This block captures an image from the webcam and saves it to:`);
        Generator.addCode(`# Windows: C:\\Users\\{your user name}\\webcam_images`);
        Generator.addCode(`# MacOS: /Users/{your user name}/webcam_images`);
        Generator.addCode(`# Linux: /home/{your user name}/webcam_images`);
    }

    //% block="Load custom model [MODEL_NAME]" blockType="reporter"
    //% MODEL_NAME.shadow="string" MODEL_NAME.defl="'mobilenet_NOME_v1.keras'"
    export function load_custom_model(parameter: any, block: any) {
        let model_name = parameter.MODEL_NAME.code;
        Generator.addImport(`from learn import load_custom_model`);
        Generator.addCode(`load_custom_model(${model_name})`);

        // Add comments
        Generator.addCode(`# This block loads a custom trained model from:`);
        Generator.addCode(`# Local files: ~/MAST_learn/test/model.keras`);
        Generator.addCode(`# URLs: https://github.com/user/repo/raw/main/model.keras`);
        Generator.addCode(`# Downloaded models cached in: ~/MAST_learn/models_cache/`);
    }

    //% block="Predict image [IMAGE_PATH] with custom model [MODEL] using classes [CLASS_NAMES]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="'image.jpg'"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function predict_image_custom(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import predict_image_custom`);
        Generator.addCode(`predict_image_custom(${model}, ${image_path}, ${class_names})`);

        // Add comments
        Generator.addCode(`# Returns tuple: (predicted_class, confidence_score)`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
        Generator.addCode(`# If class_names is None, uses default classes`);
    }

    //% block="Get label from image [IMAGE_PATH] with model [MODEL] using classes [CLASS_NAMES]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="'image.jpg'"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function predict_image_label(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import predict_image_label`);
        Generator.addCode(`predict_image_label(${model}, ${image_path}, ${class_names})`);
        
        // Add comments
        Generator.addCode(`# Returns only the predicted label (string)`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
    }

    //% block="Get confidence from image [IMAGE_PATH] with model [MODEL] using classes [CLASS_NAMES]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="'image.jpg'"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function predict_image_confidence(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import predict_image_confidence`);
        Generator.addCode(`predict_image_confidence(${model}, ${image_path}, ${class_names})`);
        
        // Add comments
        Generator.addCode(`# Returns only the confidence score (float 0.0-1.0)`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
    }

    //% block="Get label from webcam with model [MODEL] from camera [CAMERA_INDEX] using classes [CLASS_NAMES]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function webcam_predict_label(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let camera_index = parameter.CAMERA_INDEX.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import webcam_predict_label`);
        Generator.addCode(`webcam_predict_label(${model}, ${camera_index}, ${class_names})`);
        
        // Add comments
        Generator.addCode(`# Capture + predict: returns only label (string)`);
        Generator.addCode(`# Use pre-loaded model object for efficiency`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
    }

    //% block="Get confidence from webcam with model [MODEL] from camera [CAMERA_INDEX] using classes [CLASS_NAMES]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function webcam_predict_confidence(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let camera_index = parameter.CAMERA_INDEX.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import webcam_predict_confidence`);
        Generator.addCode(`webcam_predict_confidence(${model}, ${camera_index}, ${class_names})`);
        
        // Add comments
        Generator.addCode(`# Capture + predict: returns only confidence (float 0.0-1.0)`);
        Generator.addCode(`# Use pre-loaded model object for efficiency`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
    }

    //% block="Webcam predict with model [MODEL_NAME] from camera [CAMERA_INDEX] using classes [CLASS_NAMES]" blockType="reporter"
    //% MODEL_NAME.shadow="string" MODEL_NAME.defl="'mobilenet_NOME_v1.keras'"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function webcam_predict(parameter: any, block: any) {
        let model_name = parameter.MODEL_NAME.code;
        let camera_index = parameter.CAMERA_INDEX.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import webcam_predict`);
        Generator.addCode(`webcam_predict(${model_name}, ${camera_index}, ${class_names})`);

        // Add comments
        Generator.addCode(`# Complete workflow: capture image + load model + predict`);
        Generator.addCode(`# Returns tuple: (predicted_class, confidence_score)`);
        Generator.addCode(`# Use Mind+ list blocks to create class_names list`);
        Generator.addCode(`# If class_names is None, uses default classes`);
    }

}