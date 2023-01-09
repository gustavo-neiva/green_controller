def post_worker_init(worker):
    from green_controller.app import start_controller
    start_controller()
