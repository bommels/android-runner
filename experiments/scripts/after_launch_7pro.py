# noinspection PyUnusedLocal,PyUnusedLocal
def main(device, *args, **kwargs):
    # # """ Enable for Web Experiments using Chrome
    print('total RUN #:', args)
    if 'com.android.chrome' in args[2]:
        # if is first run of experiment:
        # if args[1][1] == 1:
        print('Accept Chrome policy prompts')
        # # Tap coordinates can be found by enabling 'Pointer location' in Developer options
        # # Accept Chrome policy prompts
        device.shell('input tap 729 2795') # TODO only at the very start of the entire experiment?
        device.shell('input tap 162 2788')
        
        # Enable permissions for Chrome
        device.shell('pm grant com.android.chrome android.permission.RECORD_AUDIO')
        device.shell('pm grant com.android.chrome android.permission.CAMERA')
        device.shell('pm grant com.android.chrome android.permission.WRITE_EXTERNAL_STORAGE')
        device.shell('pm grant com.android.chrome android.permission.READ_EXTERNAL_STORAGE')
                # """

        # if args[1][1] == 2:
        # # if is 2 run of experiment:
        #     print('Remove lite mode popup')
        #     device.shell('input tap 250 917')
    pass
