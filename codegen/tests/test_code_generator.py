import os

from src.code_generator import CodeGenerator


class TestCodeGenerator:
    def test_init(self):
        # Arrange
        openapi_file_path = "tests/data/sample.yaml"
        output_dir = "tests/data/sample_dir/"

        # Act
        code_generator = CodeGenerator(
            openapi_file_path=openapi_file_path,
            output_dir=output_dir,
            parameters=[
                "--use-union-operator",
                "--use-default-kwarg",
                "--use-double-quotes",
            ],
        )

        # Assert
        assert len(code_generator._imports) >= 3
        assert len(code_generator._classes) == 4
        class_names = {c.name for c in code_generator._classes}
        assert "Item" in class_names

    def test_execute(self):
        # Arrange
        openapi_file_path = "tests/data/sample.yaml"
        output_dir = "tests/data/sample_dir/"

        # Act
        CodeGenerator(
            openapi_file_path=openapi_file_path,
            output_dir=output_dir,
            parameters=[
                "--use-union-operator",
                "--use-default-kwarg",
                "--use-double-quotes",
            ],
        ).execute()

        # Assert
        with os.scandir(output_dir) as entries:
            files = [entry.name for entry in entries if entry.is_file()]
        assert "item.py" in files
        assert "user.py" in files
        assert "user_create.py" in files
        assert "user_update.py" in files
        assert not os.path.exists("tests/data/sample_dir/temporary_model.py")
        assert not os.path.exists("tests/data/sample_dir/temporary_api.yaml")

        # Verify array/nested generic import logic works
        with open(os.path.join(output_dir, "user.py"), "r", encoding="utf-8") as f:
            user_py_content = f.read()
        assert "from tests.data.sample_dir.item import Item" in user_py_content
