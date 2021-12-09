from odoo import models


class ThemeAviato(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_aviato_post_copy(self, mod):
        self.disable_view('website.footer_custom')
        self.enable_view('website.template_footer_contact')
        self.enable_view('website.template_footer_slideout')

        self.enable_asset("website.ripple_effect_scss")
        self.enable_asset("website.ripple_effect_js")