import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, browserHistory, IndexRoute} from 'react-router';
import App from './App';
import Board from './Board'
import './css/bootstrap.min.css'
import './css/style.css'

ReactDOM.render(
  (
    <Router history={browserHistory}>
      <Route path="/" component={App}>
        <IndexRoute component={Board} />
      </Route>
    </Router>
  ),
  document.getElementById('root')
);
