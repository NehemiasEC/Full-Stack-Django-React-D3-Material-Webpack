import React from 'react';
import {Component} from 'react';
import Button from "@material-ui/core/Button"


class App extends Component{

    constructor(props){
        super(props);
    }


    render(){
        return (
            <Button variant="contained" color="primary">
                Hola mundo
            </Button>
        )
    }
}

export default App;