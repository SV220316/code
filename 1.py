from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout

class CameraApp(App):
    def build(self):
        # Set up the layout and camera widget
        layout = BoxLayout(orientation='vertical')
        
        # Create a Camera widget and set it to play the video feed
        camera = Camera(play=True)  # "play=True" starts the live feed
        layout.add_widget(camera)
        
        return layout

if __name__ == "__main__":
    CameraApp().run()
