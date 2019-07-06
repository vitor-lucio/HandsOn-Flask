from flask import render_template, Blueprint, url_for, redirect



principal = Blueprint('principal', __name__)

@principal.route('/')
def indef():
	
	return "Hello World"