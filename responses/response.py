class Response:
    @staticmethod
    def formatValidationErrors(errors):
        errors_list = []
            
        for error in errors:
            for err in errors[error]:
                errors_list.append(f"Param {error}: {err}")

        return errors_list