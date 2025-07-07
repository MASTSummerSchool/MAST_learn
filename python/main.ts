//% color="#F7AD45" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Train decision tree from [FILENAME]" blockType="reporter"
    //% FILENAME.shadow="string" FILENAME.defl="train"
    export function train_decision_tree(parameter: any, block: any) {
        // Initiating the variables as strings removing trailing and leading spaces
        let filename = parameter.FILENAME.code;

        // Add import statement
        Generator.addImport(`from learn import train_decision_tree`);

        // Add the actual code for the training
        Generator.addCode(`train_decision_tree(${filename})`);

        // Add comments OS dependant
        Generator.addCode(`# This block LOAD the sensor data FROM:`)
        Generator.addCode(`# Windows: C:\\Users\\{your user name}\\sensor_data`)
        Generator.addCode(`# MacOS: /Users/{your user name}/sensor_data`)
        Generator.addCode(`# Linux: /home/{your user name}/sensor_data`)
        Generator.addCode(`# Please enter ONLY the filename in the block (e.g. data)`)

        // return the code
        return null;
    }

    //% block="Train neural network with [FILENAME]" blockType="reporter"
    //% FILENAME.shadow="string" FILENAME.defl="train"
    export function train_neural_network(parameter: any, block: any) {
        let filename = parameter.FILENAME.code;
        Generator.addImport(`from learn import train_neural_network`);
        Generator.addCode(`train_neural_network(${filename})`);
    }

    //% block="Test [MODEL] to get label from [DATA]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'trained model'"
    //% DATA.shadow="list" DATA.defl="'read sensor data'"
    export function infer(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let data = parameter.DATA.code;
        Generator.addImport(`from learn import infer`);
        Generator.addCode(`infer(${model}, ${data})`);
    }

    //% block="Get label from [MODEL] using [DATA]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'trained model'"
    //% DATA.shadow="list" DATA.defl="'read sensor data'"
    export function get_label(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let data = parameter.DATA.code;
        Generator.addImport(`from learn import get_label`);
        Generator.addCode(`get_label(${model}, ${data})`);
    }

    //% block="Get confidence score from [MODEL] using [DATA]" blockType="reporter"
    //% MODEL.shadow="normal" MODEL.defl="'trained model'"
    //% DATA.shadow="list" DATA.defl="'read sensor data'"
    export function get_confidence_score(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let data = parameter.DATA.code;
        Generator.addImport(`from learn import get_confidence_score`);
        Generator.addCode(`get_confidence_score(${model}, ${data})`);
    }

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

    //% block="Predict image [IMAGE_PATH] with custom model [MODEL]" blockType="reporter"
    //% IMAGE_PATH.shadow="string" IMAGE_PATH.defl="'image.jpg'"
    //% MODEL.shadow="normal" MODEL.defl="'custom_model'"
    export function predict_image_custom(parameter: any, block: any) {
        let image_path = parameter.IMAGE_PATH.code;
        let model = parameter.MODEL.code;
        Generator.addImport(`from learn import predict_image_custom`);
        Generator.addCode(`predict_image_custom(${model}, ${image_path})`);
    }

    //% block="Webcam predict with model [MODEL_NAME] from camera [CAMERA_INDEX]" blockType="reporter"
    //% MODEL_NAME.shadow="string" MODEL_NAME.defl="'mobilenet_NOME_v1.keras'"
    //% CAMERA_INDEX.shadow="math_number" CAMERA_INDEX.defl="0"
    export function webcam_predict(parameter: any, block: any) {
        let model_name = parameter.MODEL_NAME.code;
        let camera_index = parameter.CAMERA_INDEX.code;
        Generator.addImport(`from learn import webcam_predict`);
        Generator.addCode(`webcam_predict(${model_name}, ${camera_index})`);
    }

}
