from django.core.exceptions import ValidationError


def validate_pic_type(pic):
    type_of_pic = pic.file.name
    if 'jpg' not in type_of_pic and 'jpeg' not in type_of_pic and 'png' not in type_of_pic:
        raise ValidationError('Please select JPG or PNG file')
    return pic


def validate_size(file):
    actual_size = file.file.size
    if actual_size > 5242880:
        raise ValidationError('Upload Up To 5 MB')
    return file


def validate_ai_file_type(file):
    type_of_file = file.file.name
    if 'pickle' not in type_of_file and 'xml' not in type_of_file and 'json' not in type_of_file:
        raise ValidationError('only Pickle,XML and JSON allowed')
    return file


def validate_notebook_type(file):
    type_of_file = file.file.name
    if 'ipynb' not in type_of_file:
        raise ValidationError('only Notebooks/ipynb allowed')
    return file