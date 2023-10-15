import wf_datagen
import wf_dataprocessing

if __name__ == '__main__':
    try:
        wf_datagen.main()
        pass
    except KeyboardInterrupt:
        print('Finished')