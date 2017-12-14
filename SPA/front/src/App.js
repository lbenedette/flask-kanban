import React, {Component} from 'react';
import './css/style.css';

class App extends Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    return (
      <div>
        <div className="container-fluid">
          <div className="row">
            <nav className="navbar navbar-default navbar-static-top">
              <div className="container-fluid">
                <div className="navbar-header">
                  <a className="navbar-brand" href="#">Kanban</a>
                </div>
              </div>
            </nav>
          </div>
        </div>

        <div className="container-fluid">
          <div className="row">
            <div className="col-sm-4">
              <div className="panel panel-danger">
                <div className="panel-heading">
                  <h3 className="panel-title text-center">
                    TO DO
                    <a href="#"><span className="glyphicon glyphicon-plus pull-right" aria-hidden="true"></span></a>
                  </h3>
                </div>
                <div className="panel-body">
                  {/*todo itens*/}
                </div>
              </div>
            </div>
            <div className="col-sm-4">
              <div className="panel panel-warning">
                <div className="panel-heading">
                  <h3 className="panel-title text-center">
                    DOING
                    <a href="#"><span className="glyphicon glyphicon-plus pull-right" aria-hidden="true"></span></a>
                  </h3>
                </div>
                <div className="panel-body">
                  {/*doing itens*/}
                </div>
              </div>
            </div>
            <div className="col-sm-4">
              <div className="panel panel-success">
                <div className="panel-heading">
                  <h3 className="panel-title text-center">
                    DONE
                    <a href="#"><span className="glyphicon glyphicon-plus pull-right" aria-hidden="true"></span></a>
                  </h3>
                </div>
                <div className="panel-body">
                  {/*done itens*/}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
