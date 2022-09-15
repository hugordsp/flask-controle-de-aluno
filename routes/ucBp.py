from flask import Blueprint, render_template
from ..extensions import db
from ..models.uc import Uc

#Instanciar Blueprint
ucBp = Blueprint('ucBp', __name__)

@ucBp.route('/uc')
def uc_list():
    #return "Voltamos às 20h50"
    #adciona isso
    #db.create_all()

    ucs_query = Uc.query.all()
    return render_template('uc_lista.html', ucs=ucs_query)
