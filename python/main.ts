//% color="#F7AD45" iconWidth=50 iconHeight=40
// Ensure Generator is defined as an object with addImport and addCode methods
declare const Generator: {
    addImport: (importStr: string) => void;
    addCode: (codeStr: string) => void;
};

namespace robot {

    //% block="Capture image from webcam [CAMERA_INDEX]" blockType="reporter"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    export function capture_webcam_image(parameter: any, block: any) {
        let camera_index = parameter.CAMERA_INDEX.code;
        Generator.addImport(`from learn import capture_webcam_image`);
        Generator.addCode(`capture_webcam_image(${camera_index})`);
    }

    //% block="Load custom model [MODEL_NAME]" blockType="reporter"
    //% MODEL_NAME.shadow="string" MODEL_NAME.defl="'mobilenet_NOME_v1.keras'"
    export function load_custom_model(parameter: any, block: any) {
        let model_name = parameter.MODEL_NAME.code;
        Generator.addImport(`from learn import load_custom_model`);
        Generator.addCode(`load_custom_model(${model_name})`);
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
    }

    //% block="Verify model compatibility [MODEL_PATH]" blockType="reporter"
    //% MODEL_PATH.shadow="string" MODEL_PATH.defl="'model.keras'"
    export function verify_model_compatibility(parameter: any, block: any) {
        let model_path = parameter.MODEL_PATH.code;
        Generator.addImport(`from learn import verify_model_compatibility`);
        Generator.addCode(`verify_model_compatibility(${model_path})`);
    }

    //% block="Convert model format: [INPUT_PATH] to [TARGET_FORMAT]" blockType="reporter"
    //% INPUT_PATH.shadow="string" INPUT_PATH.defl="'model.keras'"
    //% TARGET_FORMAT.shadow="string" TARGET_FORMAT.defl="'h5'"
    export function convert_model_format(parameter: any, block: any) {
        let input_path = parameter.INPUT_PATH.code;
        let target_format = parameter.TARGET_FORMAT.code;
        Generator.addImport(`from learn import convert_model_format`);
        Generator.addCode(`convert_model_format(${input_path}, target_format=${target_format})`);
    }

}