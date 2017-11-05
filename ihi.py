import sublime
import sublime_plugin


class PepperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if (self.view.is_read_only()):
            self.view.set_read_only(False)
            #self.view.set_status('toggle_readonly', '')
            self.view.window().status_message('editleyiniz')
            #self.window.set_menu_visible(False)
        else:
            self.view.set_read_only(True)
            #self.view.set_status('toggle_readonly', 'Readonly')
            self.view.window().status_message('riid onli')

            #selam bebek
            
