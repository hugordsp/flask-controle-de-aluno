from flask import Blueprint
from ..extensions import db
from ..models.uc import uc

#Instanciar Blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
    #return "Voltamos às 20h50"
    #adciona isso
    db.create_all()
