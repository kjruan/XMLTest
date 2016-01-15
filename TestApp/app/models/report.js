var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var reportSchema = new Schema({
	name: String,
	date: Date,
	datasets: []
})