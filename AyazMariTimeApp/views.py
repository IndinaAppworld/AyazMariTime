import csv
import io
import re
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dateparse import parse_date
from .models import DumpData, VTMaster, VSMaster, RANKMaster, FLAGMaster, CURRENCYMaster, SHIP2Master, PUMPMaster, \
    ENGMaster, VISAMaster, SCMaster, PAYMaster, ONBOARD_CHOICES


def parse_fk(model, value, field='title'):
    try:
        if not value:
            # If value is empty, look for object with title="NIL"
            return model.objects.get(**{field: 'NIL'})

        # Normalize the input
        lookup_value = value.strip().upper() if isinstance(value, str) else value
        return model.objects.get(**{field: lookup_value})

    except model.DoesNotExist:
        return None
    except Exception as e:
        print(f"Error in parse_fk for model {model.__name__}: {e}")
        return None


def extract_numeric_amounts(lines):
    for line in lines:
        line = line.strip()
        match = re.search(r'\d+(?:,\d{3})*(?:\.\d+)?', line)
        if match:
            number = match.group().replace(',', '')
            return number  # Return the first number found
    return None  # If no number is found



def parse_date_safe(value):
    try:
        return parse_date(value) if value else None
    except:
        return None
# Create a reverse mapping: {'YES': '1', 'NO': '2', 'GAP': '3'}
ONBOARD_REVERSE = {label.upper(): key for key, label in ONBOARD_CHOICES}

def upload_csv(request):
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        decoded_file = csv_file.read().decode("utf-8")
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=reader.fieldnames + ["Status"])
        writer.writeheader()

        for row in reader:
            status = ""
            try:
                customid = row['ID'].strip().upper() if row['ID'] else None
                data = {
                    'name': row['name'].upper(),
                    'vt': parse_fk(VTMaster, row['vt']),
                    'vs': parse_fk(VSMaster, row['vs']),
                    'rank': parse_fk(RANKMaster, row['rank']),
                    'rank2': parse_fk(RANKMaster, row['rank2']),
                    'mobno': row['mobno'],
                    'emailid': row['emailid'].upper(),
                    'flag': parse_fk(FLAGMaster, row['flag']),
                    'pay1': ((row['pay1'])) if row['pay1'] else None,
                    'pay2': ((row['pay2'])) if row['pay2'] else None,
                    'currency': parse_fk(CURRENCYMaster, row['currency']),
                    'alvdate':datetime.strptime(row['avldate'], '%d/%m/%Y').strftime('%Y-%m-%d') if row['avldate'] else None,
                    'onb': ONBOARD_REVERSE.get(row['onb'].strip().upper(), '4') if row.get('onb') else '4',
                    'ship2': parse_fk(SHIP2Master, row['ship2']),
                    'pump': parse_fk(PUMPMaster, row['pump']),
                    'eng': parse_fk(ENGMaster, row['eng']),
                    'dob': parse_date_safe(row['dob']),
                    'cdc': row['cdc'].upper(),
                    'passport': row['passport'].upper(),
                    'visa': parse_fk(VISAMaster, row['visa']),
                    'agn': row['agn'].upper(),
                    'sc': parse_fk(SCMaster, row['sc']),
                    'pay': parse_fk(PAYMaster, row['pay']),
                    'cno': row['cno'].upper(),
                    'comp': row['comp'].upper(),
                    'vf': row['vf'].upper(),
                    'vn': row['vn'].upper(),
                    'doc': parse_date_safe(row['doc']),
                    'so': parse_date_safe(row['so']),
                    'sof': parse_date_safe(row['sof']),
                    'doc1': parse_date_safe(row['doc1']),
                    'remarks': row['remarks'].upper(),
                    'updatedate': datetime.now(),
                }

                if customid:
                    obj, created = DumpData.objects.update_or_create(
                        customid=customid,
                        defaults=data
                    )
                    status = "Inserted" if created else "Updated"
                else:
                    obj = DumpData.objects.create(**data)
                    status = "Inserted (new, no customid)"

            except Exception as e:
                status = f"Failed: {str(e)}"

            row["Status"] = status
            writer.writerow(row)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="upload_result.csv"'
        response.write(output.getvalue())
        return response

    return render(request, "admin/upload_csv.html")
