from app import app
import time

@app.route('/')
@app.route('/api/time')
def get_current_time():
    return {'local_time': time.ctime(time.time())}