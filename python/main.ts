//% color="#F7AD45" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Capture image from webcam [CAMERA_INDEX]" blockType="reporter"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    export function capture_webcam_image(parameter: any, block: any) {
        let camera_index = parameter.CAMERA_INDEX.code;
        Generator.addImport(`from learn import capture_webcam_image`);
        Generator.addCode(`capture_webcam_image(${camera_index})`);
        Generator.addCode(`# Returns the path of the captured image as a string`);
    }

    //% block="Load custom model [MODEL_NAME]" blockType="reporter"
    //% MODEL_NAME.shadow="string" MODEL_NAME.defl="'mobilenet_NOME_v1.keras'"
    export function load_custom_model(parameter: any, block: any) {
        let model_name = parameter.MODEL_NAME.code;
        Generator.addImport(`from learn import load_custom_model`);
        Generator.addCode(`load_custom_model(${model_name})`);

        // Add comments
        Generator.addCode(`# This block loads a custom trained model from:`);
        Generator.addCode(`# Local files: ~/models/model.keras`);
        Generator.addCode(`# URLs: https://github.com/user/repo/raw/main/model.keras`);
        Generator.addCode(`# Downloaded models cached in: ~/models/cache/`);
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

    //% block="Get label from existing image [IMAGE_PATH] with model [MODEL] using classes [CLASS_NAMES]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="capture_webcam_image(0)"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function predict_label_from_image(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import predict_label_from_image`);
        Generator.addCode(`predict_label_from_image(${image_path}, ${model}, ${class_names})`);
        Generator.addCode(`# IMAGE_PATH must be a valid file path, e.g. the output of capture_webcam_image`);
    }

    //% block="Get confidence from existing image [IMAGE_PATH] with model [MODEL] using classes [CLASS_NAMES]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="capture_webcam_image(0)"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    export function predict_confidence_from_image(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        let class_names = parameter.CLASS_NAMES.code;
        Generator.addImport(`from learn import predict_confidence_from_image`);
        Generator.addCode(`predict_confidence_from_image(${image_path}, ${model}, ${class_names})`);
        Generator.addCode(`# IMAGE_PATH must be a valid file path, e.g. the output of capture_webcam_image`);
    }

    //% block="Send prediction data: image [IMAGE_PATH] label [LABEL] confidence [CONFIDENCE] to API [API_URL]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="'image.jpg'"
    //% LABEL.shadow="string" LABEL.defl="'predicted_label'"
    //% CONFIDENCE.shadow="math_number" CONFIDENCE.defl="0.95"
    //% API_URL.shadow="string" API_URL.defl="https://petoiupload.vercel.app/api/predict"
    export function send_prediction_data(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let label = parameter.LABEL.code;
        let confidence = parameter.CONFIDENCE.code;
        let api_url = parameter.API_URL.code;
        Generator.addImport(`from learn import send_prediction_data`);
        Generator.addCode(`send_prediction_data(${image_path}, ${label}, ${confidence}, ${api_url})`);

        // Add comments
        Generator.addCode(`# Sends JSON with base64 image, label, confidence to REST API`);
        Generator.addCode(`# Returns API response or error information`);
        Generator.addCode(`# Includes timestamp and automatic error handling`);
    }

    //% block="Webcam predict and send: model [MODEL] camera [CAMERA_INDEX] classes [CLASS_NAMES] to API [API_URL]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    //% CLASS_NAMES.shadow="normal" CLASS_NAMES.defl="'class_list'"
    //% API_URL.shadow="string" API_URL.defl="https://petoiupload.vercel.app/api/predict"
    export function webcam_predict_and_send(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let camera_index = parameter.CAMERA_INDEX.code;
        let class_names = parameter.CLASS_NAMES.code;
        let api_url = parameter.API_URL.code;
        Generator.addImport(`from learn import webcam_predict_and_send`);
        Generator.addCode(`webcam_predict_and_send(${model}, ${camera_index}, ${class_names}, ${api_url})`);

        // Add comments
        Generator.addCode(`# Complete workflow: capture + predict + send to API`);
        Generator.addCode(`# Returns combined prediction and API response data`);
        Generator.addCode(`# Automatic error handling and status reporting`);
    }

    //% block="Verify model compatibility [MODEL_PATH]" blockType="reporter"
    //% MODEL_PATH.shadow="string" MODEL_PATH.defl="'model.keras'"
    export function verify_model_compatibility(parameter: any, block: any) {
        let model_path = parameter.MODEL_PATH.code;
        Generator.addImport(`from learn import verify_model_compatibility`);
        Generator.addCode(`verify_model_compatibility(${model_path})`);

        // Add comments
        Generator.addCode(`# Diagnoses model loading issues and compatibility`);
        Generator.addCode(`# Returns detailed information about the model file`);
        Generator.addCode(`# Useful for debugging .keras file problems`);
    }

    //% block="Convert model format: [INPUT_PATH] to [TARGET_FORMAT]" blockType="reporter"
    //% INPUT_PATH.shadow="string" INPUT_PATH.defl="'model.keras'"
    //% TARGET_FORMAT.shadow="string" TARGET_FORMAT.defl="'h5'"
    export function convert_model_format(parameter: any, block: any) {
        let input_path = parameter.INPUT_PATH.code;
        let target_format = parameter.TARGET_FORMAT.code;
        Generator.addImport(`from learn import convert_model_format`);
        Generator.addCode(`convert_model_format(${input_path}, target_format=${target_format})`);

        // Add comments
        Generator.addCode(`# Converts between .keras, .h5, and saved_model formats`);
        Generator.addCode(`# Solves compatibility issues between TensorFlow versions`);
        Generator.addCode(`# Returns path to converted model file`);
    }

}