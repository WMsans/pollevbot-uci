"""Answer the first option of a poll that a presenter opens on pollev.com."""

from patchright.sync_api import sync_playwright

PROFILE = ".browser-profile"


def run(presenter_code, wait_time=60 * 60 * 2):
    ms = wait_time * 1000

    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE,
            headless=False,
            no_viewport=True,
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()

        try:
            page.goto("https://pollev.com/login")
            input("Log in in the browser window (finish Duo), then press Enter here to start monitoring...")
            # Duo can land anywhere; the code box lives on /home.
            page.goto("https://pollev.com/home")

            # Join using a presenter's code
            join_presenter_by_code(page, presenter_code, ms)

            # Interact with the session options
            select_first_option(page, ms)

            # Refresh the page to ensure updates are fetched
            page.reload()

        except Exception as e:
            print(f"Error during processing: {e}")

        finally:
            input("Press Enter to quit")
            ctx.close()


def join_presenter_by_code(page, code, timeout):
    """Enters the presenter's code to join the session."""
    page.locator("#participate_home_form_presenter").fill(code, timeout=timeout)
    page.locator('[name="button"]').first.click(timeout=timeout)


def select_first_option(page, timeout):
    """Selects the first multiple-choice option available."""
    page.locator(".component-response-multiple-choice__option__vote").first.click(timeout=timeout)


if __name__ == "__main__":
    present_code = "irenegassko734"
    run(present_code)
