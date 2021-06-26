import json
import math
 
class SrtExporter():
    def sec_to_hms(self, seconds):
        hours = seconds//3600
        mins = (seconds % 3600)//60
        secs = int((seconds % 3600)%60)
        return (hours, mins, secs)

    def export(self, transcript_json, encoding = None):
        """
           
            :param file: file_path of SRT file
            :param encoding: Encoding if present
 
        """
        i = 1
        file = ''
        for data in transcript_json:
            start = data['start']
            stop = data['end']
            content = data['text']
            file +='{}\n'.format(i)
            converted_start_time = self.sec_to_hms(start)
            hour = converted_start_time[0]
            minute = converted_start_time[1]
            sec = converted_start_time[2]

            minisec = int(math.modf(start)[0] * 1000)
            file += str(hour).zfill(2) +':' + str(minute).zfill(2) +':' + str(sec).zfill(2) +',' + str(minisec). zfill(3)

            file += ' --> '
            
            converted_stop_time = self.sec_to_hms(stop)
            hour = converted_stop_time[0]
            minute = converted_stop_time[1]
            sec = converted_stop_time[2]

            minisec = abs(int(math.modf(stop)[0] * 1000)) + 1
            file += str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(sec).zfill(2) + ',' + str(minisec).zfill(3)
            file +='\n' + content +'\n\n'
            i += 1

        with open('test.srt', 'w', encoding='utf-8') as f:
            f.write(file)