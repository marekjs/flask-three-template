from flask import render_template, request
import sys


def errors_handlers(app):
    """
        Registers application errors handlers.
    """

    development = app.config["DEVELOPMENT"]

    @app.errorhandler(Exception)
    def exception_handler(error):
        """Handle uncaught exceptions."""
        exc_info = sys.exc_info()
        app.logger.error("Uncaught Exception", exc_info=exc_info)

        # try to log the exception also in db
        app.reports.try_log_exception(exc_info[1])

        if development:
            # display error details in console
            print("ERROR: " + str(error))

        app.handle_exception(error)


    @app.errorhandler(400)
    def bad_request(error):
        """Handle 400 errors."""
        return render_template("error/400.html"), 400


    @app.errorhandler(401)
    def not_authorized(error):
        """Handle 401 errors."""
        return render_template("error/401.html"), 401


    @app.errorhandler(403)
    def forbidden(error):
        """Handle 403 errors."""
        return render_template("error/403.html"), 403


    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return render_template("error/404.html"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        """Handle 405 errors."""
        return render_template("error/405.html", method=request.method), 405


    @app.errorhandler(500)
    def internal_server_error(error):
        """Handle 500 errors."""
        if app.config["DEVELOPMENT"]:
            # send error details
            return error.message, 500
        return render_template("error/500.html"), 500

