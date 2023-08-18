from odoo import fields,models,api
from odoo.exceptions import UserError, ValidationError

class FileCheckerPdf(models.Model):
    _name = "file.checker"
    _decription = "File Checker"
    
    file = fields.Binary(string='file', attachment=True)

    filename = fields.Char()



    @api.constrains('file', 'filename')

    def get_data(self):

        if not self.filename.endswith('.pdf'):     # check if file pdf

            raise ValidationError('This file is not PDF')

        else:
            raise ValidationError('This file is PDF')

        
