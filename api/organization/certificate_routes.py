from api.lib import *
from api.organization.organization import Certificate, CertificateModel


router = APIRouter(
    prefix="/api/certificate",
    tags=["Certificate"]
)


@router.get("/")
def get_all_certificates():
    return json.loads(Certificate.objects().to_json())


@router.get("/{certificate_id}")
def get_certificate(certificate_id: str):
    return json.loads(Certificate.objects(id=certificate_id).get().to_json())


@router.post("/")
def create_certificate(data: CertificateModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    certificate = Certificate(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        graduation=data.graduation,
        user=user
    ).save()
    return json.loads(certificate.to_json())


@router.put("/{certificate_id}")
def update_certificate(certificate_id: str, data: CertificateModel, token: str = Depends(JWTBearer)):
    certificate = Certificate.objects(id=certificate_id)
    validate_authority(token, certificate.get().user.pk)
    certificate.update_one(
        title=data.title,
        image=data.image,
        institution=data.institution,
        address=data.address,
        timeline=data.timeline,
        description=data.description,
        activities=data.activities,
        graduation=data.graduation,
    )
    return json.loads(certificate.get().to_json())


@router.delete("/{certificate_id}")
def delete_certificate(certificate_id: str, token: str = Depends(JWTBearer())):
    validate_authority(token, certificate_id)
    return Certificate(id=certificate_id).delete()
