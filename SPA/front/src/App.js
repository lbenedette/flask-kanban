import React, {Component} from 'react';
import $ from 'jquery';


class App extends Component {
  constructor() {
    super();
    this.state = {todo: [], doing: [], done: []};
  }

  componentDidMount() {
    $.ajax({
        url: 'http://127.0.0.1:5000/api/tasks',
        dataType: 'json',
        success: function (response) {
          this.setState({todo: response.todo, doing: response.doing, done: response.done});
        }.bind(this)
      }
    );
  }

  moveTask(task_id, status, event) {
    event.preventDefault();
    $.ajax({
        url: 'http://127.0.0.1:5000/api/task/update/' + task_id + '/' + status,
        dataType: 'json',
        success: function (response) {
          this.setState({todo: response.todo, doing: response.doing, done: response.done});
        }.bind(this)
      }
    );
  }

  deleteTask(task_id, status, event) {
    event.preventDefault();
    $.ajax({
        url: 'http://127.0.0.1:5000/api/task/delete/' + task_id,
        dataType: 'json',
        success: function (response) {
          this.setState({[status]: response.tasks});
        }.bind(this)
      }
    );
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
                  {
                    this.state.todo.map(function (task) {
                      return (
                        <div className="well well-sm" key={task.id}>
                          <div className="text-center">
                            <a onClick={this.deleteTask.bind(this, task.id, 'todo')}><span className="glyphicon glyphicon-remove-circle" aria-hidden="true"></span></a>
                            <a onClick={this.moveTask.bind(this, task.id, 'doing')}><span className="glyphicon glyphicon-circle-arrow-right pull-right" aria-hidden="true"></span></a>
                          </div>
                          <div className="text-justify task">
                            {task.text}
                          </div>
                        </div>
                      )
                    }.bind(this))
                  }
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
                  {
                    this.state.doing.map(function (task) {
                      return (
                        <div className="well well-sm" key={task.id}>
                          <div className="text-center">
                            <a href="#"><span className="glyphicon glyphicon-remove-circle" aria-hidden="true"></span></a>
                            <a onClick={this.moveTask.bind(this, task.id, 'done')}><span className="glyphicon glyphicon-circle-arrow-right pull-right" aria-hidden="true"></span></a>
                            <a onClick={this.moveTask.bind(this, task.id, 'todo')}><span className="glyphicon glyphicon-circle-arrow-left pull-left" aria-hidden="true"></span></a>
                          </div>
                          <div className="text-justify task">
                            {task.text}
                          </div>
                        </div>
                      )
                    }.bind(this))
                  }
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
                  {
                    this.state.done.map(function (task) {
                      return (
                        <div className="well well-sm" key={task.id}>
                          <div className="text-center">
                            <a href="#"><span className="glyphicon glyphicon-remove-circle" aria-hidden="true"></span></a>
                            <a onClick={this.moveTask.bind(this, task.id, 'doing')}><span className="glyphicon glyphicon-circle-arrow-left pull-left" aria-hidden="true"></span></a>
                          </div>
                          <div className="text-justify task">
                            {task.text}
                          </div>
                        </div>
                      )
                    }.bind(this))
                  }
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
