import React, {Component} from 'react';


class App extends Component {

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

        {this.props.children}

      </div>
    );
  }
}

export default App;
