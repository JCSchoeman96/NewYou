defmodule NewYou.Audit.EvidenceRecord do
  use Ash.Resource,
    otp_app: :new_you,
    domain: NewYou.Audit,
    data_layer: AshPostgres.DataLayer

  postgres do
    table "evidence_records"
    repo NewYou.Repo
  end

  actions do
    read :read do
      primary? true
      public? false
    end

    create :materialize do
      accept [:obligation_id]
      public? false
    end
  end

  attributes do
    uuid_v7_primary_key :id

    create_timestamp :created_at
  end

  relationships do
    belongs_to :obligation, NewYou.Audit.EvidenceObligation do
      allow_nil? false
      attribute_writable? true
      public? false
    end
  end

  identities do
    identity :one_record_per_obligation, [:obligation_id],
      message: "already has a materialised evidence record"
  end
end
