import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class DigitValidator(object):
	def validate(self, password, user=None):
		if not re.findall('\d', password):
			raise ValidationError(
				_("The password must contain at least 3 digits, 0 to 9"), code='password_no_digit',)


	def get_help_text(self):
		return _("password must containa the minimum of 3 digits")


class UpperCaseValidator(object):
	def validate(self, password, user=None):
		if not re.findall('[A-Z]', password):
			raise ValidationError(
				_("The first two characters must be uppercase !, A-Z"), code="password_no_upper",
			)

	def get_help_text(self):
		return _(
			"Your password must contain at least 2 uppercase characters"
		)


class LowerCaseValidator(object):
	def validate(self, password, user=None):
		if not re.findall('[a-z]', password):
			raise ValidationError(
				_("The first two characters must be lowercase !, a-z"), code="password_no_lower",
			)

	def get_help_text(self):
		return _(
			"Your password must contain at least 1 lowercase character"
		)


class SymbolValidator(object):
	def validate(self, password, user=None):
		if not re.findall('[()[\]{}|\\`~!@#$%^&_\-+;:\'",<>./?]', password):
			raise ValidationError(
				_("Your password must contain at least 1 symbol") , code="password_no_symbol",
			)

	def get_help_text(self):
		return _(
			"Your password must contain at least 1 symbol"
		)


class LengthValidator(object):
	def validate(self, password, user=None):
		if len(password) < 16:
			raise ValidationError(
				_("Your password must be greater than or equal to 16 characters"), code="password_lenght_error"
			)

	def get_help_text(self):
		return _(
			"Your password must be greater than or equal to 16 characters"
		)