from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Ind_Profile, Clims, CompanyDetails
from .storage import upload_files_to_drive


@api_view(['POST'])
def profile_data(request):
    # Create a new instance of Ind_Profile with the provided data
    filename = request.data.get('file_name')
    uploaded_file = request.FILES.get('file')  # Retrieve the uploaded file
    
    g_path = upload_files_to_drive(uploaded_file,filename)
    
    profile = Ind_Profile(
        id=len(Ind_Profile.objects.all())+1,
        userid=int(request.data.get('userid')),
        first_name=request.data.get('first_name'),
        last_name=request.data.get('last_name'),
        profile_bio=request.data.get('profile_bio', 'the bio not filled yet.'),
        contact_number=request.data.get('contact_number'),
        location=request.data.get('location'),
        skills=request.data.get('skills'),
        resume_image= g_path,
        usr_type=request.data.get('usr_type')
    )
    
    # Save the profile instance to the database
    profile.save()
    
    return Response({'success': True, 'message': 'Data stored successfully.',"g_path":g_path})

@api_view(['POST'])
def Store_Company_Details(request):
    try:
        print("get len")
        obj = len(CompanyDetails.objects.all())
    except:
        obj = 0
    print(obj,"length is")
    company = CompanyDetails(
        id=obj,
        company_name=request.data.get('company_name'),
        company_email=request.data.get('company_email'),
        company_number=request.data.get('company_number'),
        company_linkedin=request.data.get('company_linkedin'),
        company_location=request.data.get('company_location'),
        company_bio=request.data.get('company_bio'),
        start_year=request.data.get('start_year'),
        no_of_emp=request.data.get('no_of_emp'),
        logo=request.data.get('logo'),
    )
    print("created..")
    
    # Save the company details to the database
    company.save()
    
    return Response({'success': True, 'message': 'Company details stored successfully.'})

@api_view(['POST'])
def Rec_Profile_data(request):
    # Create a new instance of Ind_Profile with the provided data
    filename = request.data.get('file_name')
    uploaded_file = request.FILES.get('file')  # Retrieve the uploaded file
    
    g_path = upload_files_to_drive(uploaded_file,filename)
    
    profile = Ind_Profile(
        id=len(Ind_Profile.objects.all())+1,
        userid=int(request.data.get('userid')),
        name=request.data.get('name'),
        email=request.data.get('email'),
        profile_bio=request.data.get('profile_bio'),
        contact_number=request.data.get('contact_number'),
        location=request.data.get('location'),
        linked_in=request.data.get('linked_in'),
        no_of_emp=request.data.get('no_of_emp'),
        start_date = request.data.get('start_date'),
        logo = request.data.get('start_date'),
    )
    
    # Save the profile instance to the database
    profile.save()
    
    return Response({'success': True, 'message': 'Data stored successfully.',"g_path":g_path})


@api_view(['POST'])
def clim_data(request):
    clim = Clims(
        callback_id=request.data.get('callback_id'),
        status=request.data.get('status'),
        repo=request.data.get('repo'),
        template_id=request.data.get('template_id')
    )
    
    # Save the clim instance to the database
    clim.save()
    
    return Response({'success': True, 'message': 'Data stored successfully.'})
