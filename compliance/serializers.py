from rest_framework import serializers
from .validators.helper import province_decode_from_cnic, parse_income
from .utils import NTNChoices, ntn_choices

class CNICSerializer(serializers.Serializer):
    cnic = serializers.CharField(max_length=15, required=True)

    def validate(self, attrs):
        cnic = attrs.get('cnic').strip().replace("-", "")
        if not cnic:
            raise serializers.ValidationError("CNIC is required.")
        if not cnic.isdigit() or len(cnic) != 13:
            raise serializers.ValidationError("Invalid CNIC format. It should be a 13-digit number.")
        province = province_decode_from_cnic(cnic)
        if province == "Unknown Province":
            raise serializers.ValidationError("Invalid CNIC province code.")
        attrs['cnic'] = cnic
        attrs['province'] = province

        return attrs


class NTNSerializer(serializers.Serializer):
    ntn = serializers.CharField(max_length=15, required=True)
    choice = serializers.ChoiceField(choices=ntn_choices, required=True)

    def validate(self, attrs):
        ntn = attrs.get('ntn').strip()
        choice = attrs.get('choice')
        if not choice:
            raise serializers.ValidationError("NTN type is required.")
        if choice not in dict(ntn_choices):
            raise serializers.ValidationError("Invalid choice for NTN type.")
        if not ntn:
            raise serializers.ValidationError("NTN is required.")
        if not ntn.isdigit():
            raise serializers.ValidationError("Invalid NTN format. It should be a numeric value.")
        if choice == NTNChoices.INDIVIDUAL and len(ntn) != 13:
            raise serializers.ValidationError("Invalid NTN format for Individual. It should be a 13-digit number.")
        if choice == NTNChoices.COMPANY:
            if len(ntn) == 8:
                if "-" in ntn:
                    split_data = ntn.split("-")
                    if len(split_data[0]) != 7:
                        raise serializers.ValidationError("Invalid NTN format for Company. The first part should be 7 digits.")
            else:
                raise serializers.ValidationError("Invalid NTN format for Company. It should be a 8-digit number.")
        
        attrs['ntn'] = ntn
        attrs['choices'] = "Individual" if choice == NTNChoices.INDIVIDUAL else "Company"
        return attrs


class TaxBracketSerializer(serializers.Serializer):
    annual_salary = serializers.CharField(max_length=100)


    def validate(self, attrs):
        income = attrs.get("annual_salary")
        if not income:
            raise serializers.ValidationError("annual_salary is required")
        amount = parse_income(income)
        if amount < 0:
            raise serializers.ValidationError("annual_salary cannot be negative.")
        attrs['annual_salary'] = amount
        return attrs
