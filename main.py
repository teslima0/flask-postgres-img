from project import create_app
app =create_app()
import sys

sys.setrecursionlimit(1500)


if __name__ == '__main__':
    app.run(debug=True)