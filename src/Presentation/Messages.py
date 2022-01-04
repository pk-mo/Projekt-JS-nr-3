import dearpygui.dearpygui as dpg

success_message_tag = 'success_message'
error_message_tag = 'error_message'
product_price_message_tag = 'price_message'
product_amount_message_tag = 'amount_message'
selected_product_message_tag = 'selected_product_message'
inserted_coins_message_tag = 'inserted_coins_message'
withdrawn_coins_message_tag = 'withdrawn_coins_message'

selected_product_default_message = 'Select product'
inserted_coins_default_message = 'Insert coins'


def render_alert_messages() -> None:
    """Renders alert messages."""
    dpg.add_text(color=[0, 255, 0], tag=success_message_tag)  # Success messages
    dpg.add_text(color=[255, 0, 0], tag=error_message_tag)  # Error messages


def render_product_messages() -> None:
    """Renders messages related to products."""
    dpg.add_text(selected_product_default_message, tag=selected_product_message_tag)  # Selected product message
    dpg.add_spacer(height=20)
    dpg.add_text(color=[0, 0, 255], tag=product_price_message_tag)  # Product price message
    dpg.add_text(color=[0, 0, 255], tag=product_amount_message_tag)  # Product amount in the machine message


def render_coins_messages() -> None:
    """Renders messages related to coins."""
    dpg.add_text(inserted_coins_default_message, tag=inserted_coins_message_tag)
    dpg.add_text(tag=withdrawn_coins_message_tag)


def add_success_message(message: str) -> None:
    """Adds new success message."""
    dpg.set_value(success_message_tag, message)


def add_error_message(message: str) -> None:
    """Adds new error message."""
    dpg.set_value(error_message_tag, message)


def add_selected_product_message(message: str) -> None:
    """Adds new selected product message."""
    dpg.set_value(selected_product_message_tag, message)


def add_product_price_message(message: str) -> None:
    """Adds new product price message."""
    dpg.set_value(product_price_message_tag, message)


def add_product_amount_message(message: str) -> None:
    """Adds new product amount message."""
    dpg.set_value(product_amount_message_tag, message)


def add_inserted_coins_message(message: str) -> None:
    """Adds new inserted coins message."""
    dpg.set_value(inserted_coins_message_tag, message)


def add_withdrawn_coins_message(message: str) -> None:
    """Adds new withdrawn coins message."""
    dpg.set_value(withdrawn_coins_message_tag, message)


def reset_success_message() -> None:
    """Resets success message to its default value."""
    dpg.set_value(success_message_tag, '')


def reset_error_message() -> None:
    """Resets error message to its default value."""
    dpg.set_value(error_message_tag, '')


def reset_selected_product_message() -> None:
    """Resets selected product message to its default value."""
    dpg.set_value(selected_product_message_tag, selected_product_default_message)


def reset_product_price_message() -> None:
    """Resets product price message to its default value."""
    dpg.set_value(product_price_message_tag, '')


def reset_product_amount_message() -> None:
    """Resets product amount message to its default value."""
    dpg.set_value(product_amount_message_tag, '')


def reset_inserted_coins_message() -> None:
    """Resets inserted coins message to its default value."""
    dpg.set_value(inserted_coins_message_tag, inserted_coins_default_message)


def reset_withdrawn_coins_message() -> None:
    """Resets withdrawn coins message to its default value."""
    dpg.set_value(withdrawn_coins_message_tag, '')
