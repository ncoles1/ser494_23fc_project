import wf_datagen
import wf_dataprocessing
import wf_visualization

if __name__ == '__main__':
    try:
        wf_datagen.main()
        wf_dataprocessing.main()
        wf_visualization.main()
    except KeyboardInterrupt:
        print('Finished')