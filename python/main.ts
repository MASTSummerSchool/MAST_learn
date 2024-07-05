//% color="#F7AD45" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Train decision tree from [FILENAME] where target name is [LABEL]" blockType="reporter"
    //% FILENAME.shadow="string" FILENAME.defl="data"
    //% LABEL.shadow="string" LABEL.defl="label"
    export function train_decision_tree(parameter: any, block: any) {
        // Initiating the variables as strings removing trailing and leading spaces
        let filename = parameter.FILENAME.code;
        let label = parameter.LABEL.code;

        // Add import statement
        Generator.addImport(`from learn import train_decision_tree`);

        // Add the actual code for the training
        Generator.addCode(`train_decision_tree(${filename}, ${label})`);

        // Add comments OS dependant
        Generator.addCode(`# This block LOAD the sensor data FROM:`)
        Generator.addCode(`# Windows: C:\\Users\\{your user name}\\sensor_data`)
        Generator.addCode(`# MacOS: /Users/{your user name}/sensor_data`)
        Generator.addCode(`# Linux: /home/{your user name}/sensor_data`)
        Generator.addCode(`# Please enter ONLY the filename in the block (e.g. data)`)

        // return the code
        return null;
    }

    //% block="Train neural network with [FILENAME] where target name is [LABEL]" blockType="reporter"
    //% FILENAME.shadow="string" FILENAME.defl="test"
    //% LABEL.shadow="string" LABEL.defl="label"
    export function train_neural_network(parameter: any, block: any) {
        let filename = parameter.FILENAME.code;
        let label = parameter.LABEL.code;
        Generator.addImport(`from learn import train_neural_network`);
        Generator.addCode(`train_neural_network(${filename}, ${label})`);
    }

    //% block="Infer label with [MODEL] from condition [CONDITION]" blockType="command"
    //% MODEL.shadow="normal" MODEL.defl="'trained model'"
    //% CONDITION.shadow="list" CONDITION.defl="'timestamp', 'pir', 'touch', 'light', 'ir'"
    export function infer(parameter: any, block: any) {
        let model = parameter.MODEL.code;
        let condition = parameter.CONDITION.code;
        Generator.addImport(`from learn import infer`);
        Generator.addCode(`infer(${model}, ${condition})`);
    }

}
