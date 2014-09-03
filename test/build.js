/**
  * Module dependencies.
  */
var builder = require('component-hooks');
var path = require('path');
var cwd = path.join(__dirname);

// exec

builder(cwd)
  .copy()
  .standalone()
  .dev()
  .end(function(err){
    if (err){
      console.log(err);
      process.exit(1);
    }
  });