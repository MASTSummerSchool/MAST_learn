//% color="#458EF7" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Train decision tree with [PATH] where target name is [TARGET]" blockType="reporter"
    //% PATH.shadow="string" PATH.defl="data.csv"
    //% TARGET.shadow="string" TARGET.defl="target"
    export function train_decision_tree(parameter: any, block: any) {
        let data_path = parameter.PATH.code
        let target = parameter.TARGET.code
        Generator.addImport(`from learn import train_decision_tree`);
        Generator.addCode(`train_decision_tree(${data_path}, ${target})`);
    }

    //% block="Train neural network with [PATH] where target name is [TARGET]" blockType="reporter"
    //% PATH.shadow="string" PATH.defl="data.csv"
    //% TARGET.shadow="string" TARGET.defl="target"
    export function train_neural_network(parameter: any, block: any) {
        let data_path = parameter.PATH.code
        let target = parameter.TARGET.code
        Generator.addImport(`from learn import train_neural_network`);
        Generator.addCode(`train_neural_network(${data_path}, ${target})`);

    }

    //% block="Infer label with [MODEL] from condition [CONDITION]" blockType="command"
    //% MODEL.shadow="normal"
    //% CONDITION.shadow="list" PATH.defl="['timestamp', 'pir', 'touch', 'light', 'ir']"
    export function infer(parameter: any, block: any) {
        let model = parameter.MODEL.code
        let condition = parameter.CONDITION.code
        Generator.addImport(`from learn import infer`);
        Generator.addCode(`infer(${model}, ${condition})`);
    }

}
