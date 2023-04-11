# 2. (необов'язкове виконання) Написати власний менеджер контексту, задачею якого буде друкувати "==========" – 10 знаків
# дорівнює перед виконанням коду та після виконання коду, таким чином виділяючи блок коду символами дорівнює.

class MyContextManager:
    def __enter__(self):
        print("=" * 10)
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("=" * 10)

with MyContextManager() as my_manager:
    print("Something inside my context manager")
