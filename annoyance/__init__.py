import importlib.abc
import importlib.resources
import random
import win10toast


class Annoyance:
    def __init__(self) -> None:
        self.toaster = win10toast.ToastNotifier()

    def get_icon(self) -> importlib.abc.Traversable:
        package_icons = importlib.resources.files(__package__) / "icons"
        return random.choice(list(package_icons.iterdir()))

    def show(self) -> None:
        with importlib.resources.as_file(self.get_icon()) as icon:
            self.toaster.show_toast(
                title="Hi Goose :)",
                msg=f"I loves you! Enjoy this picture of {icon.stem}",
                icon_path=icon,
            )
