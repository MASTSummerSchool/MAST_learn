//% color="#458EF7" iconWidth=50 iconHeight=40
namespace robot {

    //% block="Train decision tree with [PATH] where target name is [TARGET]" blockType="reporter"
    //% PATH.shadow="string" PATH.defl="data"
    //% TARGET.shadow="string" TARGET.defl="target"
    export function train_decision_tree(parameter: any, block: any) {
        let path = JSON.stringify(parameter.PATH.code);
        let target = JSON.stringify(parameter.TARGET.code);
        Generator.addImport(`from learn import train_decision_tree`);
        Generator.addCode(`train_decision_tree(${path}, ${target})`);
        Generator.addCode(`# Questo blocco CARICA i dati del sensore DAI seguenti directory:`)
        Generator.addCode(`# Windows: C:\\Users\\{il tuo nome utente}\\sensor_data`)
        Generator.addCode(`# MacOS: /Users/{il tuo nome utente}/sensor_data`)
        Generator.addCode(`# Linux: /home/{il tuo nome utente}/sensor_data`)
        Generator.addCode(`# Inserire SOLO il nome del file nel blocco (es. data)`)
    }

    //% block="Train neural network with [PATH] where target name is [TARGET]" blockType="reporter"
    //% PATH.shadow="string" PATH.defl="data"
    //% TARGET.shadow="string" TARGET.defl="target"
    export function train_neural_network(parameter: any, block: any) {
        let path = JSON.stringify(parameter.PATH.code);
        let target = JSON.stringify(parameter.TARGET.code);
        Generator.addImport(`from learn import train_neural_network`);
        Generator.addCode(`train_neural_network(${path}, ${target})`);
        Generator.addCode(`# Questo blocco CARICA i dati del sensore DAI seguenti directory:`)
        Generator.addCode(`# Windows: C:\\Users\\{il tuo nome utente}\\sensor_data`)
        Generator.addCode(`# MacOS: /Users/{il tuo nome utente}/sensor_data`)
        Generator.addCode(`# Linux: /home/{il tuo nome utente}/sensor_data`)
        Generator.addCode(`# Inserire SOLO il nome del file nel blocco (es. data)`)
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
