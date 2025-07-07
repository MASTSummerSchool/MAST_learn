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
        Generator.addCode(`# Windows: C:\\Users\\{your user name}\\MAST_learn\\test`);
        Generator.addCode(`# MacOS: /Users/{your user name}/MAST_learn/test`);
        Generator.addCode(`# Linux: /home/{your user name}/MAST_learn/test`);
    }

    //% block="Create class list [CLASS1] [CLASS2] [CLASS3] [CLASS4] [CLASS5] [CLASS6] [CLASS7] [CLASS8]" blockType="reporter"
    //% CLASS1.shadow="string" CLASS1.defl="'class1'"
    //% CLASS2.shadow="string" CLASS2.defl="'class2'"
    //% CLASS3.shadow="string" CLASS3.defl="'class3'"
    //% CLASS4.shadow="string" CLASS4.defl="'class4'"
    //% CLASS5.shadow="string" CLASS5.defl="'class5'"
    //% CLASS6.shadow="string" CLASS6.defl="'class6'"
    //% CLASS7.shadow="string" CLASS7.defl="'class7'"
    //% CLASS8.shadow="string" CLASS8.defl="'class8'"
    export function create_class_list(parameter: any, block: any) {
        let class1 = parameter.CLASS1.code;
        let class2 = parameter.CLASS2.code;
        let class3 = parameter.CLASS3.code;
        let class4 = parameter.CLASS4.code;
        let class5 = parameter.CLASS5.code;
        let class6 = parameter.CLASS6.code;
        let class7 = parameter.CLASS7.code;
        let class8 = parameter.CLASS8.code;
        Generator.addImport(`from learn import create_class_list`);
        Generator.addCode(`create_class_list(${class1}, ${class2}, ${class3}, ${class4}, ${class5}, ${class6}, ${class7}, ${class8})`);
        
        // Add comments
        Generator.addCode(`# Creates a list of class names for your custom model`);
        Generator.addCode(`# Use this list with predict_image_custom or webcam_predict`);
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
        Generator.addCode(`# If class_names is None, uses default classes`);
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
        Generator.addCode(`# If class_names is None, uses default classes`);
    }

}